

##### Para baixar as dependencias
```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```


##### Exemplo de requisicao local
```bash
$ http://127.0.0.1:5000/sunrise?latitude=36.7201600&longitude=-4.4203400&eventtype=sunset
```


##### Exemplo de requisicao no Render
```bash
$ https://sunrise-r8nq.onrender.com/sunrise?latitude=36.7201600&longitude=4.4203400&eventtype=sunset
```