FROM centos:7.5.1804

RUN yum update -y
RUN yum install -y wget bzip2 which

# R install
RUN yum -y install epel-release
RUN yum -y install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
RUN yum install -y R

# Anaconda install (Python 3.6.6)
RUN wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh && \
  sh Anaconda3-5.3.0-Linux-x86_64.sh -b -p /usr/anaconda3 && \
  rm Anaconda3-5.3.0-Linux-x86_64.sh
ENV PATH /usr/anaconda3/bin:$PATH

# Install cdt (Causal Discovery Toolbox) for python
RUN wget https://github.com/Diviyan-Kalainathan/CausalDiscoveryToolbox/archive/master.zip &&\
    unzip master.zip &&\
    cd CausalDiscoveryToolbox-master &&\
    pip install -r requirements.txt &&\
    python setup.py install develop --user
RUN pip install munkres
