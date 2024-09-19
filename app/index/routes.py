from app.index import bp
from flask import render_template, redirect
from app.services.LeageAPI import LeagueAPI


@bp.route('/', methods=['GET', 'POST'])
def reroute():
    return redirect('/jacksonville')


@bp.route('/<string:Slug>', methods=['GET', 'POST'])
@bp.route('/index/<string:Slug>', methods=['GET', 'POST'])
def index(Slug):
    api = LeagueAPI("https://gql.poolplayers.com/graphql")
    league = api.query_league(slug=Slug)
    divisions = api.query_divisions(slug=Slug, session_id=league['data']['league']['currentSessionId'])

    print(league)
    print(divisions)

    return render_template('index/index.html', league=league, divisions=divisions)
