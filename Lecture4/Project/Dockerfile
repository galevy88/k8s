# Base Image alpine
FROM node:14-alpine

# Specifying Work Dir
WORKDIR /usr/app

# Copy Files
COPY ./pacage.json ./
RUN npm install
COPY ./ ./

# start command npm start
CMD ["npm", "start"]