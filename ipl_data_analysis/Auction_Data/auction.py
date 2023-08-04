
class AuctionDataParser:

    def final_purse_details(self,teams):
        final_purse = []
        headers = [header.text for header in teams.find_all('th')]
        step_size = len(headers)
        final_purse.append(headers)

        count = 1
        each_team = []

        for team in teams.find_all('td'):
            each_team.append(team.text.strip())
            if count % step_size == 0:
                final_purse.append(each_team)
                each_team = []
            count = count + 1

        return final_purse

    def sold_players_details(self,players_sold_per_team,teams):
        players_sold = []
        headers = [header.text for header in players_sold_per_team[0].find_all('th')]
        step_size = len(headers)
        players_sold.append(headers+['TEAM'])

        for team,players_per_team in zip(teams,players_sold_per_team):
            each_player = []
            count = 1
            for player in players_per_team.find_all('td'):
                each_player.append(player.text.strip())
                if count % step_size == 0:
                    each_player.append(team)
                    players_sold.append(each_player)
                    each_player = []
                count = count + 1

        return players_sold

    def unsold_players_details(self,players):
        players_unsold = []
        headers = [header.text for header in players.find_all('th')]
        step_size = len(headers)
        players_unsold.append(headers)

        count = 1
        each_player = []

        for player in players.find_all('td'):
            each_player.append(player.text.strip())
            if count % step_size == 0:
                players_unsold.append(each_player)
                each_player = []
            count = count + 1

        return players_unsold