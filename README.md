# personal-portfolio

Website: https://cantella.dev/

I am always working on new ways to host my website using various technologies, here is what I've experimented on until now.

Docker containers managed with docker-compose on a bare-metal server (RaspberryPi):
- Nginx production server redirecting requests to django and wordpress
- Django production server with gunicorn
- Wordpress container
- MariaDB (stores wordpress data)
- Cloudflared container (SSL Tunnel to Cloudflare servers) to avoid security risks related to hosting on my homelab

Azure App Service:
 - Django production server
