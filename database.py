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

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)

def add_app_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)")
    conn.execute(statement=query, parameters=dict(
                job_id=job_id,
                full_name=data['full_name'],
                email=data['email'],
                linkedin_url=data['linkedin_url'],
                education=data['education'],
                experience=data['experience'],
                resume_url=data['resume_url']))
    