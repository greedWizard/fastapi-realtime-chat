DC = docker-compose
APP_FILE = docker_compose/app.yaml
SERVICES = docker_compose/storages.yaml

.PHONY: app
app:
	${DC} -f ${APP_FILE} up --build -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${SERVICES} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${SERVICES} down

.PHONY: services
services:
	${DC} -f ${SERVICES} up --build -d

.PHONY: drop-service
drop-services:
	${DC} -f ${SERVICES} down

.PHONY: app-logs
app-logs:
	${DC} -f ${APP_FILE} logs -f
