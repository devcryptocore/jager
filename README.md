# jager
<strong>Obtener la ubicación exácta de un dispositivo, con un enlace.</strong>
<p></p><img src="jager.png">

<p>Esta herramienta, crea un servidor en tu dispositivo, a partir de php y lo muestra a internet, a través de un tunel ssh</p>
<br>generando un enlace, el cual dirige a una página, la cual usa ingeniería social, para hacer que la víctima habilte el permiso de ubicación.
<p>De esta manera, se obtiene las coordenadas del dispositivo que reciba el enlace.</p>
<p>Es importante que antes de ejecutar el script, use el comando "ssh -R 80:localhost:3333 nokey@localhost.run" y escriba "yes" cuando se requiera.</p>
<h2>Instalación:</h2>
<p>pip install -r requirements.txt</p>
<p>[-] apt install php</p>
<p>[-] apt install openssh</p>
<p>[-] pip install requirements.txt</p>
<p>[-] ssh -R 80:localhost:3333 nokey@localhost.run</p>
<p>[-] yes</p>
<h2>Uso</h2>
<p>[-] cd jager</p>
<p>[-] python jager.py</p>

<p>https://t.me/+NzJDZaOyojE1ZTZh</p>

Demo:
https://www.youtube.com/watch?v=FQSs0fwb7Xw
