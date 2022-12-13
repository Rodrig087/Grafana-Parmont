FROM grafana/grafana:9.2.2

# Set Grafana options
ENV GF_ENABLE_GZIP=true
#ENV GF_USERS_DEFAULT_THEME=light

# Paths
ENV GF_PATHS_PROVISIONING="/etc/grafana/provisioning"
ENV GF_PATHS_PLUGINS="/var/lib/grafana/plugins"

###### Customization ########################################
USER root

# Replace Favicon
COPY img/favicon_v2.png /usr/share/grafana/public/img/fav32.png
# Replace Logo
COPY img/logo_V6.svg /usr/share/grafana/public/img/grafana_icon.svg

# Background
#COPY img/background_azul.svg /usr/share/grafana/public/img/g8_login_dark.svg

# Update Javascript
# Replace Titles
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|"AppTitle","Grafana")|"AppTitle","Parmont Instruments")|g' {} \;
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|"LoginTitle","Welcome to Grafana")|"LoginTitle","Parmont Instruments")|g' {} \;
# Delete Footer
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|{target:"_blank",id:"documentation",text:"Documentation",icon:"document-info",url:"https://grafana.com/docs/grafana/latest/?utm_source=grafana_footer"},{target:"_blank",id:"support",text:"Support",icon:"question-circle",url:"https://grafana.com/products/enterprise/?utm_source=grafana_footer"},{target:"_blank",id:"community",text:"Community",icon:"comments-alt",url:"https://community.grafana.com/?utm_source=grafana_footer"}||g' {} \;
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|{target:"_blank",id:"version",text:`${e.edition}${s}`,url:t.licenseUrl}||g' {} \;
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|{target:"_blank",id:"version",text:`v${e.version} (${e.commit})`,url:i?`https://grafana.com/docs/grafana/${l}/release-notes/release-notes-${o}/`:void 0}||g' {} \;
RUN find /usr/share/grafana/public/build/ -name *.js -exec sed -i 's|{target:"_blank",id:"updateVersion",text:"New version available!",icon:"download-alt",url:"https://grafana.com/grafana/download?utm_source=grafana_footer"}||g' {} \;

#############################################################

#USER grafana