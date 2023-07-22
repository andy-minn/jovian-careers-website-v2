from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
  db_conn_str,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs