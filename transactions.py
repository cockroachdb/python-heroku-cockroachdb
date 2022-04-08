from models import Score
import uuid

def get_scores_txn(session):
    query = session.query(Score)
    return query.all()

def add_score_txn(session, avatar, playername, points):
    score = Score(
        id=str(
            uuid.uuid4()),
        avatar=avatar,
        playername=playername,
        points=points
    )
    session.add(score)

