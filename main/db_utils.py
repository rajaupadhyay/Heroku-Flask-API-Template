from main import db
from main.models import DBTemplate


def checkRowExistence(name, email):
    query1 = DBTemplate.query.filter(DBTemplate.name == name).filter(DBTemplate.email == email)
    return (len(query1.all()) == 0, query1)

def insertRow(name, email):
    try:
        rowDoesNotExist, _ = checkRowExistence(name, email)

        if rowDoesNotExist:
            rowAdder = DBTemplate(name=name, email=email)
            db.session.add(rowAdder)
            db.session.commit()

            res = "Added row to PGSQL, ID: {}".format(rowAdder.id)
            return (res)
        else:
            res = "A row with name={} and email={} already exists in the database".format(name, email)
            return (res)
    except Exception as e:
        print(str(e))
        return (None)


def deleteRow(name, email):
    rowDoesNotExist, queryCursor = checkRowExistence(name, email)

    if not rowDoesNotExist:
        print('DELETING RECORD {} {} {}'.format(name, email))
        queryCursor.delete()
        db.session.commit()


def updateRow(name, email):
    try:
        row = DBTemplate.query.filter(DBTemplate.name == name).filter(DBTemplate.email == email).first()
        row.name = name
        db.session.commit()
        return 'Data updated successfully for {}/{}'.format(name, email)
    except Exception as e:
        return 'Unable to update data for {}/{} {}'.format(name, email, e)


def readRow(name, email):
    rowDoesNotExist, queryCursor = checkRowExistence(name, email)

    if not rowDoesNotExist:
        print('\n\n Found data regarding following : {} \n\n'.format(name))
        for row in queryCursor:
            email = row.email
            break
    return (email)

def retrieveAllRows():
    dataVals = DBTemplate.query.all()
    return([x.email for x in dataVals])