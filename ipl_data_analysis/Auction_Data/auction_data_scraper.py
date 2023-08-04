import requests
from bs4 import BeautifulSoup
import csv
import os

from auction import AuctionDataParser

years = [2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013]

for year in years:

    final_purse_file = f'Auction_Data/purse/final_purse_{year}.csv'
    players_sold_file = f'Auction_Data/sold/players_sold_{year}.csv'
    players_unsold_file = f'Auction_Data/unsold/players_unsold_{year}.csv'

    os.makedirs(os.path.dirname(final_purse_file),exist_ok=True)
    os.makedirs(os.path.dirname(players_sold_file),exist_ok=True)
    os.makedirs(os.path.dirname(players_unsold_file),exist_ok=True)

    final_purse_csv = open(final_purse_file,'w',encoding='utf-8')
    players_sold_csv = open(players_sold_file,'w',encoding='utf-8')
    players_unsold_csv = open(players_unsold_file,'w',encoding='utf-8')

    final_purse_writer = csv.writer(final_purse_csv)
    players_sold_writer = csv.writer(players_sold_csv)
    players_unsold_writer = csv.writer(players_unsold_csv)

    url = f'https://www.iplt20.com/auction/{year}'

    response = requests.get(url).text

    soup = BeautifulSoup(response,'lxml')

    auction_data = AuctionDataParser()

    final_purse = soup.find('div',class_='ih-pcard-sec')
    final_purse = auction_data.final_purse_details(final_purse)
    final_purse_writer.writerows(final_purse)

    teams = [team.text.strip() for team in soup.find_all('div',class_='ih-titel')]
    players_sold_per_team = soup.find_all('table',id='t1')
    players_sold = auction_data.sold_players_details(players_sold_per_team,teams)
    players_sold_writer.writerows(players_sold)

    players_unsold = soup.find('table',id='t2')
    players_unsold = auction_data.unsold_players_details(players_unsold)
    players_unsold_writer.writerows(players_unsold)

    final_purse_csv.close()
    players_sold_csv.close()
    players_unsold_csv.close()