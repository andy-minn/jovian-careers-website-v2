from sqlalchemy import create_engine, text

db_conn_str = "mysql+pymysql://xiqvi2ps6xtblut22w1j:pscale_pw_nDAwEchf9iAh44vDbfDG8v2ErKGqU02ojBNXtPFC29L@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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