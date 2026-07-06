class football_team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def find_player(self, number):
        for player in self.players:
            if player["number"] == number:
                return player
        return None

    def add_player(self, name, position, number, age, nationality):
        if self.find_player(number) is not None:
            print(
                f"Error: number {number} is already taken by another player.")
            return

        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)
        print(f"player {name} added to the team")

    def remove_player(self, number):
        player = self.find_player(number)
        if player is None:
            print(f"Player with number {number} is not found!")
            return
        self.players.remove(player)
        print(f"Player with number {number} has been removed from the team.")

    def update_player(self, number, **kwargs):
        player = self.find_player(number)
        if player is None:
            print(f"Player with number {number} was not found!")
            return

        for key, value in kwargs.items():
            player[key] = value
        print(f"Player's information with number {number} has been updated.")

    def show_team_info(self):
        print(f"Team name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print(f"Players: ")
        if not self.players:
            print("Players are not in the Team!")
        for player in self.players:
            print(
                f"{player['number']} {player['name']} - {player['position']} - {player['age']} - {player['nationality']}")

    def show_player_info(self, number):
        player = self.find_player(number)
        if player is None:
            print(f"player with number {number} was not found in the team!")
            return
        print(f"Player information (number {number}):")
        for key, value in player.items():
            print(f"{key} : {value}")


if __name__ == "__main__":
    team = football_team("Dinamo Tbilisi", "Levan Khomeriki")

    team.add_player("Giorgi mamardzashvili", "Goalkeeper", 1, 23, "Georgia")
    team.add_player("Khvicha kvaratskkhelia", "Forward", 7, 22, "Georgia")
    team.show_team_info()
    team.update_player(7, goal=9, assist=10)
    team.show_player_info(7)
    team.remove_player(1)
    team.show_team_info()
