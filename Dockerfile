#Stage 1 Choosing image for work
FROM python:3.8.9-alpine3.13 as prepare
WORKDIR /usr/src/app
# Copy application to image
COPY application/ .
# installing tools and extracting dependencies to the file
RUN pip install pip-tools  \
 && python3 -m piptools compile 

# Stage 2. Choosing clean image
FROM python:3.8.9-alpine3.13 as build
WORKDIR /usr/src/app
# Copy requirements.txt and application  file from previous stage
COPY --from=prepare /usr/src/app/ . 
# Install dependencies, application, adding non-root user and group, change permissions
RUN pip install --no-cache-dir -r requirements.txt && python3 setup.py install \
                       && addgroup -g 10001 pyapp \
                       && adduser -D -h /usr/src/app -u 10000  pyapp -G pyapp \ 
                       && chown pyapp:pyapp /usr/src/app  \
                       && chmod 755 /usr/src/app 
USER pyapp
EXPOSE 8080
ENTRYPOINT ["python3","-m"]
CMD ["demo"]    
