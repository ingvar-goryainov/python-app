FROM python:3.9-alpine3.16  as base

ENV NON_ROOT_USER=ipysmennyi
RUN adduser -D $NON_ROOT_USER -s /sbin/nologin
ENV PATH="/home/$NON_ROOT_USER/.local/bin:$PATH"
USER $NON_ROOT_USER

FROM base as build
COPY --chown=$NON_ROOT_USER ["/application", "/application"]
WORKDIR "/application"
RUN pip3 install --user .

FROM base
COPY --chown=$NON_ROOT_USER --from=build ["/home/$NON_ROOT_USER/.local", "/home/$NON_ROOT_USER/.local"]
EXPOSE 8080
ENTRYPOINT ["demo"]