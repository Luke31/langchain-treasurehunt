# Use an official Node.js runtime as the base image
FROM node:16-alpine
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the Node.js dependencies
RUN yarn install

RUN yarn global add serve

# Copy the React application code to the container
# COPY public public # mounted in volume for hot-reload
# COPY src src # mounted in volume for hot-reload

# Build the React application
# RUN yarn run build

ENV PORT=1234
EXPOSE 1234
# CMD ["serve", "-s", "build"]
CMD ["yarn", "run", "start"]
