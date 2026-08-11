# Homelab

## Descripción

Homelab personal para practicar administración de sistemas Linux, automatización y despliegue de aplicaciones. Consta de dos equipos conectados mediante SSH, usados como entorno de prácticas para DevOps

## Arquitectura
┌─────────────────────┐ SSH (llave) ┌──────────────────────┐
│ MacBook Pro M4 │ ──────────────────────────▶│ HP Pavilion x360 │
│ (estación principal)│ ssh homelab │ (servidor headless) │
└─────────────────────┘ └──────────────────────┘


## Equipos

### Mac (estación principal)
- MacBook Pro 14" M4
- 16 GB RAM / 1 TB SSD
- Usada como terminal principal de trabajo, conexión remota a la HP vía SSH.

### HP (servidor / homelab)
- HP Pavilion x360 15-dq0xxx
- Intel Core i5-8265U @ 1.60GHz
- 32 GB RAM @ 2400 MHz
- Intel UHD Graphics 620
- Ubuntu 26 LTS
- Se mantiene con la tapa cerrada, operado exclusivamente por SSH (`ssh homelab`), sin monitor ni teclado conectados.


## Seguridad

### SSH
- Autenticación exclusivamente por llave pública.
- Login root deshabilitado.

### fail2ban
Instalado y configurado para proteger el servicio SSH contra ataques de fuerza bruta:
- Máximo 5 intentos fallidos (`maxretry`) en una ventana de 10 minutos (`findtime`).
- Bloqueo de 1 hora (`bantime`) tras exceder el límite.

Verificación de estado:
\`\`\`bash
sudo fail2ban-client status ssd
\`\`\`


### Firewall (ufw)
Firewall activo con política por defecto de bloqueo de tráfico entrante. Puertos permitidos:
- 22/tcp (SSH)
- 9000/tcp (interfaz web de Portainer, para administración de contenedores Docker — accesible solo dentro de la red local, sin exposición a internet, verificado)

Verificación de estado:
\`\`\`bash
sudo ufw status verbose
\`\`\`