


class League:
    def __init__(self, id, currentSessionId, name, slug, email, phone):
        self.id = id
        self.currentSessionId = currentSessionId
        self.name = name
        self.slug = slug
        self.email = email
        self.phone = phone
        self.divisions = []

    def addDivision(self, division):
        self.divisions.append(division)


class Division:
    def __init__(self, id, name, number, format, type, nightOfPlay):
        self.id = id
        self.name = name
        self.number = number
        self.format = format
        self.type = type
        self.nightOfPlay = nightOfPlay
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)


