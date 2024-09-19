import requests


class LeagueAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def query(self, query_txt, variables):
        payload = {
            "query": query_txt,
            "variables": variables
        }

        # Send POST request and check for response status
        response = requests.post(self.base_url, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.json()

    # Data Layout: ['data']['league']
    def query_league(self, slug):
        variables = {
            "slug": slug
        }

        query_txt = '''
        query query_league($slug: String!) {
            league(slug: $slug) {
                id
                currentSessionId
                name
                slug
                email
                phone
                homePageUrl
                facebookUrl
                officeHours
                logo
                byLaws {
                    id
                    url
                __typename
                }
                __typename
            }
        }
        '''

        return self.query(query_txt, variables)

    # Data Layout: ['data']['league']['division'] (array of)
    def query_divisions(self, slug, session_id):
        variables = {
            "slug": slug,
            "session": session_id
        }

        query_txt = '''
        query leagueLayout($slug: String!, $session: Int) {
            league(slug: $slug) {
                divisions(session: $session) {
                    id
                    name
                    number
                    format
                    type
                    nightOfPlay
                    teams {
                        id
                        name
                        number
                        isBye
                    }
                }
                __typename
            }
        }
        '''

        return self.query(query_txt, variables)

    def query_division_schedule(self, division_id):
        variables = {
            "id": division_id
        }

        query_txt = '''
        query divisionSchedule($id: Int!) {
            division(id: $id) {
                id
                schedule {
                    id
                    description
                    date
                    weekOfPlay
                    skip
                    matches {
                        id
                        isBye
                        status
                        scoresheet
                        startTime
                        isPlayoff
                        location {
                            id
                            name
                            address {
                                id
                                name
                            }
                        }
                        home {
                            id
                            name
                            number
                        }
                        away {
                            id
                            name
                            number
                        }
                    }
                }
                scheduleInEdit
            }
        }
        '''

        return self.query(query_txt, variables)