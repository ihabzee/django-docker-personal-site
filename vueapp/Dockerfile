# pull official base image
FROM node:13.12.0-alpine

ARG VUE_APP_BACKEND_URL                        
ENV VUE_APP_BACKEND_URL=$VUE_APP_BACKEND_URL   
# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
# COPY package-lock.json ./
RUN npm install --silent 

## add app
# COPY . ./
#
## Uses port which is used by the actual application
#EXPOSE 3000 test commit

# start app
CMD ["npm", "run", "serve", "-- --port 3000"]