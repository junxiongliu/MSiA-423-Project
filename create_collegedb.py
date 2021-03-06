"""

This is the database creation file for the college recommendation system. Most likely, you will not need this as the database has been created.

Author: Junxiong Liu

"""

from app import db
from app.db_models import college
import pandas as pd
import logging

def create_db():
    """Create the database and table using defined db_models in SQLAlchemy. configuration parameter in __init__.py with the schema defined by models.college()

    Args:
        Null

    Returns:
        Null

    """

    # initialize db
    db.create_all()
    logger.info('Database initialization successful.')

    try:
        # add information from the existing csv
        path = 'develop/data/data_2013.csv'
        df = pd.read_csv(path,encoding='ISO-8859-1')
        logger.info('CSV successfully read in.')
    except:
        logger.warning('Unable to read original csv.')        

    try:
        # change to None to add to db
        df = df.where((pd.notnull(df)), None)

        # add to db
        for index,row in df.iterrows():
            cur_college = college(INSTNM=row['INSTNM'], CITY=row['CITY'], state=row['state'], degree_offered=row['degree_offered'],CONTROL=row['CONTROL'],region=row['region'],
                ADM_RATE=row['ADM_RATE'], SATVRMID=row['SATVRMID'], SATMTMID=row['SATMTMID'], num_undergrad=row['num_undergrad'], prop_arts_human=row['prop_arts_human'],prop_business=row['prop_business'],
                prop_health_med=row['prop_health_med'], prop_interdiscip=row['prop_interdiscip'], prop_public_svce=row['prop_public_svce'], prop_sci_math_tech=row['prop_sci_math_tech'], prop_social_sci=row['prop_social_sci'], prop_trades_personal_svce=row['prop_trades_personal_svce'])
            db.session.add(cur_college)
        logger.info('CSV successfully added to RDS.') 
    except:
        logger.warning('Error in adding into the database.') 

    try:
        # commit and close
        db.session.commit()
        db.session.close()
        logger.info('Database successfully commited.') 
    except:
        logger.info('Database commit error.') 

if __name__ == "__main__":
    # logger initialization
    logging.basicConfig(filename='createdb.log', level=logging.DEBUG)
    logger = logging.getLogger(__name__) 
    create_db()
