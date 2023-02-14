FROM ghcr.io/major/ubi-flask:7756ec0e6550c450586ac18b3bd723f473a417bb
RUN mkdir inter 
RUN yum install python3.9 -y 
COPY . /home/inter/
WORKDIR /home/inter
EXPOSE 5000
CMD ["python3", "app.py"]