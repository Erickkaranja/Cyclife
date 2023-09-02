# Cyclife project.

## Codebase formatting
While in base directory of the project (Where `Makefile` file is) run 

- to format code (should be run before any commit)
`make lint`

- to run tests
`make tests`

- clean temp files
`make clean`

## console

python console.py

- create user
(Cyclife) create user -f first_name -l last_name -e email -p password

- create bicycle
(Cyclife) create bicycle -b brand -m model -p 200 -d description

- show all objects
(Cyclife) show all

- show user 
(Cyclife) show user -u <user_id>

- show user carts
(Cyclife) show user -u <user_id> -c

- show user orders
(Cyclife) show user -u <user_id> -o

- show user reviews
(Cyclife) show user -u <user_id> -r

- show bicycles
(Cyclife) show bicycles 

- serve flask app
python -m web_flask.app

- serve api 
python -m api.v1.app
