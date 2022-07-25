# capstone_django

## Acounts

#### POST /accounts

_Formato da requisição_

```json
{
	"first_name": "Sayid",
	"last_name": "Jarrah",
	"email": "jarrahsayid@lost.com",
	"password": "wW*8uuuu"
}
```

_Formato de resposta_

```json
{
	"user_uuid": "c7e2df16-ef79-485a-a535-40dc3846151f",
	"first_name": "Sayid",
	"last_name": "Jarrah",
	"email": "jarrahsayid@lost.com",
	"created_at": "2022-07-25T13:34:17.705999Z",
	"is_staff": true,
	"is_superuser": false
}
```
#### POST /login

_Formato da requisição_

```json
{
	"email": "jarrahsayid@lost.com",
	"password": "wW*8uuuu"

}
```

_Formato de resposta_

```json
{
	"token": "ccf8b3c0fe8c3430f088c5a6cbb99c2e940de3e2"
}
```
#### GET /accounts

- Nessesario token de usuario admin


_Formato da requisição_

```json
{
	
}
```

_Formato de resposta_

```json
[
 	{
	"user_uuid": "c7e2df16-ef79-485a-a535-40dc3846151f",
	"first_name": "Sayid",
	"last_name": "Jarrah",
	"email": "jarrahsayid@lost.com",
	"created_at": "2022-07-25T13:34:17.705999Z",
	"is_staff": true,
	"is_superuser": false
	}
]
```
#### GET /accounts/<user_id>

- Nessesario token de usuario
- Apenas superusers podem buscar por outros usuarios

_Formato da requisição_

```json
{
	
}
```

_Formato de resposta_

```json
{
	"user_uuid": "c7e2df16-ef79-485a-a535-40dc3846151f",
	"first_name": "Sayid",
	"last_name": "Jarrah",
	"email": "jarrahsayid@lost.com",
	"created_at": "2022-07-25T13:34:17.705999Z",
	"is_staff": true,
	"is_superuser": false
}
```
#### PATCH /accounts/<user_id>

- Nessesario token de usuario
- Apenas superusers podem atualizar outros usuarios

_Formato da requisição_

```json
{
	"first_name": "shephard",
	"is_staff": true,
	"is_superuser": false	
}
```

_Formato de resposta_

```json
{
	"user_uuid": "c7e2df16-ef79-485a-a535-40dc3846151f",
	"first_name": "Shephard",
	"last_name": "Jarrah",
	"email": "jarrahsayid@lost.com",
	"created_at": "2022-07-25T13:34:17.705999Z",
	"is_staff": true,
	"is_superuser": false
}
```
#### DELETE /accounts/<user_id>

- Nessesario token de usuario
- Apenas superusers podem deletar outros usuarios

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
{
}
```

## Movies

#### POST /movies

- Nessesario token de usuario admin

_Formato da requisição_

```json
{
	"title": "o homem que fazia chover",
	"run_time": "135",
	"premiere": "1997-11-18",
	"classification": 12,
	"price": 27.99,
	"synopsis": "Um advogado recém formado trabalha em seu primeiro caso contra uma companhia de seguros que suspende o plano de saúde de uma vítima de leucemia...",
	"stock": {
		"quantity": 3
	},
	"genres": [
		{
			"name": "crime"
		},
		{
			"name": "drama"
		}
	]
}
```

_Formato de resposta_

```json
{
	
}
```

#### GET /movies

_Formato da requisição_

```json
{
	
}
```

_Formato de resposta_

```json
[{"title": "o homem que fazia chover",
	"run_time": "135",
	"premiere": "1997-11-18",
	"classification": 12,
	"price": 27.99,
	"synopsis": "Um advogado recém formado trabalha em seu primeiro caso contra uma companhia de seguros que suspende o plano de saúde de uma vítima de leucemia...",
	"stock": {
		"quantity": 3
	},
	"genres": [
		{
			"name": "crime"
		},
		{
			"name": "drama"
		}
	]	
}]
```
