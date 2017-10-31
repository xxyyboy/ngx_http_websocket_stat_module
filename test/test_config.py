
download_dir = "../download"
conf_file = "nginx.conf"

links = {
"pcre" : "ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.41.tar.gz",
"zlib" : "http://zlib.net/zlib-1.2.11.tar.gz",
"openssl": "http://www.openssl.org/source/openssl-1.0.2k.tar.gz",
"nginx": "http://nginx.org/download/nginx-1.13.5.tar.gz"
}
ws_backend = "http://brokerstats-test.financial.com/streaming"
ws_log_file = "logs/websocket.log"
conf_template = """
events
{{
   worker_connections 4096;
}}

http
{{
   server
   {{
      ws_log {log};
      ws_log_format "$time_local: $request_id packet from $ws_packet_source payload: $ws_payload_size";
      listen 8080;
      location /stat {{
         ws_stat;
      }}
      location /status {{
         stub_status;
      }}
      location /streaming {{
         proxy_pass {backend};
         proxy_set_header Upgrade $http_upgrade;
      }}
   }}

}}
"""