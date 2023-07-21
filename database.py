from sqlalchemy import create_engine, text

db_conn_str = "mysql+pymysql://4800c59u2iigppk8vlrp:pscale_pw_iocxD5trQZMZD2QBpfGkkfT0K1dPsRuFqkcZmN37jxq@aws.connect.psdb.cloud/joviancareers"

engine = create_engine(
  db_conn_str,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs