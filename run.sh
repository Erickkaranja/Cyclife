#!/usr/bin/env bash
# This script provides a set of functions to run different components of the Cyclife application.
# It allows the user to run the API, web app, or tests based on the provided options.
#
# Usage:
#     ./run.sh [OPTIONS]
#
# Options:
#     -h, --help                  Display this help message
#     -a, --api                   Run the API
#     -w, --web                   Run the web app
#     -t, --tests                 Run the tests
#
# Functions:
#     run_api()                   Runs the Cyclife API
#     run_web_app()               Runs the Cyclife web app
#     run_tests()                 Runs the Cyclife tests
#     usage()                     Displays the usage information
#
# Environment Variables:
#     CYCLIFE_MYSQL_USER          The MySQL username for the Cyclife database
#     CYCLIFE_MYSQL_PWD           The MySQL password for the Cyclife database
#     CYCLIFE_MYSQL_HOST          The MySQL host for the Cyclife database
#     CYCLIFE_MYSQL_DB            The MySQL database name for the Cyclife application
#     CYCLIFE_HOST                The host address for the Cyclife application
#     CYCLIFE_PORT                The port number for the Cyclife application
#
# Examples:
#     ./run.sh --api              Runs the Cyclife API
#     ./run.sh --web              Runs the Cyclife web app
#     ./run.sh --tests            Runs the Cyclife tests
function run_api() {
	CYCLIFE_MYSQL_USER=cyclife_dev \
		CYCLIFE_MYSQL_PWD=cyclifepass \
		CYCLIFE_MYSQL_HOST=localhost \
		CYCLIFE_MYSQL_DB=cyclife_dev_db \
		CYCLIFE_HOST=0.0.0.0 \
		CYCLIFE_PORT=5000 \
		python -m api.v1.app
}

function run_web_app() {
	CYCLIFE_MYSQL_USER=cyclife_dev \
		CYCLIFE_MYSQL_PWD=cyclifepass \
		CYCLIFE_MYSQL_HOST=localhost \
		CYCLIFE_MYSQL_DB=cyclife_dev_db \
		CYCLIFE_HOST=0.0.0.0 \
		CYCLIFE_PORT=5001 \
		python -m web_flask.app
}

function run_tests() {
	CYCLIFE_MYSQL_USER=cyclife_test \
		CYCLIFE_MYSQL_PWD=cyclifepass \
		CYCLIFE_MYSQL_HOST=localhost \
		CYCLIFE_MYSQL_DB=cyclife_test_db \
		pytest tests
}

usage() {
	echo "./run.sh [ -w --web, -a --api,  -t --tests]
 -h --help                    Display Help
 -w --web                     Run web app
 -t --tests                   Run tests
 -a --api                     Run api"
	return
}

#If no options provided print usage
(($#)) || usage

while [ "${1+defined}" ]; do
	case $1 in
	-a | --api)
		shift
		run_api
		;;
	-w | --web)
		shift
		run_web_app
		;;
	-t | --tests)
		shift
		run_tests
		;;
	esac
	shift
done
