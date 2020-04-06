FROM node:alpine as builder

WORKDIR '/app'
COPY package.json .
RUN npm install
COPY package*.json ./
RUN npm run build

FROM nginx
EXPOSE 80
COPY --from=builder /app/build /usr/share/nginx/html