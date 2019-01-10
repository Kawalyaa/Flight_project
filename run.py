# This file starts our app

from app import app
# The down statement of 'if' means only when this script is excuted...
# directly,the down part will run but when is imported by another..
# script the down part will not be excecuted
if __name__ == '__main__':
    app.run(debug=True)
