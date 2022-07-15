FROM traffmonetizer/cli:latest
RUN apt update && apt install python3 python3-pip -y
WORKDIR /root/webapp
ADD ./webapp /root/webapp/
RUN pip3 install --no-cache-dir -q -r /root/webapp/requirements.txt

VOLUME ["/root/.config/"]
ENV EMAIL=jcarlos1993@hotmail.com
# Expose is NOT supported by Heroku
# EXPOSE 5000
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
ENTRYPOINT ["sh", "-c", "/root/webapp/entrypoint.sh"]
