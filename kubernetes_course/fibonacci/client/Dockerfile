FROM node:alpine as builder

WORKDIR '/app'
COPY ./package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
EXPOSE 3000  # Look at lesson 141 "Multiple nginx instances"
             # The reason is that this nginx is an upstrem of the ngninx listening on port 80

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html
