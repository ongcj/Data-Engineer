docker run -d \
  --name=grafana \
  -p 3000:3000 \
  -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource,marcusolsson-json-datasource" \
  grafana/grafana