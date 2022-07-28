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
		"user_uuid": "546f4106-1a9e-4a00-a73a-bc44e3705456",
		"first_name": "Claire",
		"last_name": "Littleton",
		"email": "littletonclaire@lost.com",
		"created_at": "2022-07-23T01:03:39.295193Z",
		"is_staff": true,
		"is_superuser": false
	},
	{
		"user_uuid": "d7bf08e6-d7a9-473e-be68-0a5d4b6a4b5e",
		"first_name": "Sayid",
		"last_name": "Jarrah",
		"email": "jarrahsayid@lost.com",
		"created_at": "2022-07-25T13:56:46.453940Z",
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
	"movie_uuid": "60070cdd-0365-473d-b2c9-da45d5cb9e01",
	"title": "O Homem Que Fazia Chover",
	"run_time": "135",
	"premiere": "1997-11-18",
	"classification": 12,
	"synopsis": "Um advogado recém formado trabalha em seu primeiro caso contra uma companhia de seguros que suspende o plano de saúde de uma vítima de leucemia...",
	"price": 27.99,
	"stock": {
		"quantity": 3
	},
	"genres": [
		{
			"name": "Crime"
		},
		{
			"name": "Drama"
		}
	]
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
[
	{
		"movie_uuid": "60070cdd-0365-473d-b2c9-da45d5cb9e01",
		"title": "O Homem Que Fazia Chover",
		"run_time": "135",
		"premiere": "1997-11-18",
		"classification": 12,
		"synopsis": "Um advogado recém formado trabalha em seu primeiro caso contra uma companhia de seguros que suspende o plano de saúde de uma vítima de leucemia...",
		"price": 27.99,
		"stock": {
			"quantity": 3
		},
		"genres": [
			{
				"name": "Crime"
			},
			{
				"name": "Drama"
			}
		]
	}
]
```
## Genres

#### GET /genres

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
[
	{
		"name": "Crime"
	},
	{
		"name": "Drama"
	}
]
```

#### GET /genres/<genre_name>

_Formato da requisição_

```json
{
	
}
```

_Formato de resposta_

```json
[
	{
		"movie_uuid": "60070cdd-0365-473d-b2c9-da45d5cb9e01",
		"title": "O Homem Que Fazia Chover",
		"run_time": "135",
		"premiere": "1997-11-18",
		"classification": 12,
		"synopsis": "Um advogado recém formado trabalha em seu primeiro caso contra uma companhia de seguros que suspende o plano de saúde de uma vítima de leucemia...",
		"price": 27.99,
		"stock": {
			"quantity": 3
		},
		"genres": [
			{
				"name": "Crime"
			},
			{
				"name": "Drama"
			}
		]
	}
]
```
## Cart

#### GET /cart

- Nessesario token de usuario 

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
[
	{
		"cart_uuid": "b7dc4d39-824f-4103-93b5-36d2446a9b22",
		"total": 104.00,
		"paid": true,
		"quantity": 5,
		"movies": {
			"movie_uuid": "6830d130-6890-438b-a471-69bee9099edd",
			"title": "O Poderoso Chefão 2",
			"price": 20.99,
			"stock": {
				"quantity": 0
			}
		}
	},
	{
		"cart_uuid": "9f85c8bd-8803-476a-a52c-4fc96fb3be7a",
		"total": 104.00,
		"paid": false,
		"quantity": 5,
		"movies": {
			"movie_uuid": "b91446e4-9698-4ce5-8dfd-7f3c789e9cfa",
			"title": "O Poderoso Chefão 1",
			"price": 20.99,
			"stock": {
				"quantity": 0
			}
		}
	}
]
```

#### GET /cart/<cart_id>

- Nessesario token de usuario 

_Formato da requisição_

```json
{	
}
```

_Formato de resposta_

```json
{
		"cart_uuid": "9f85c8bd-8803-476a-a52c-4fc96fb3be7a",
		"total": 104.00,
		"paid": true,
		"quantity": 5,
		"movies": {
			"movie_uuid": "b91446e4-9698-4ce5-8dfd-7f3c789e9cfa",
			"title": "O Poderoso Chefão 1",
			"price": 20.99,
			"stock": {
				"quantity": 0
			}
		}
	}
```
#### GET /cart/pending

- Nessesario token de usuario 

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
[
	{
		"cart_uuid": "9f85c8bd-8803-476a-a52c-4fc96fb3be7a",
		"total": 104.00,
		"paid": false,
		"quantity": 5,
		"movies": {
			"movie_uuid": "b91446e4-9698-4ce5-8dfd-7f3c789e9cfa",
			"title": "O Poderoso Chefão 1",
			"price": 20.99,
			"stock": {
				"quantity": 0
			}
		}
	}
]

```
#### POST /cart/add/<movie_id>

- Nessesario token de usuario 

_Formato da requisição_

```json
{
	"quantity": 2
}
```

_Formato de resposta_

```json
{
	"cart_uuid": "ce0e13b2-1b10-488e-b36d-0cc685447ffa",
	"total": 41.98,
	"paid": false,
	"quantity": 2,
	"movies": {
		"movie_uuid": "68ca886a-878f-4a3d-befe-5a1c36b101cb",
		"title": "O Poderoso Chefão 2",
		"price": 20.99,
		"stock": {
			"quantity": 5
		}
	}
}
```
#### POST /cart/pay/

- Nessesario token de usuario 

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
{
	"status": "successful payment"
}
```
#### DELETE /cart/<cart_id>

- Nessesario token de usuario 

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
NO CONTENT
```
## Possiveis erros

#### Requisições sem o token 


_Formato da requisição_

```json
{
	"first_name": "jack",
}
```

_Formato de resposta_

```json
{
	"detail": "Invalid token header. No credentials provided."
}
```
#### Requisições com token invalido


_Formato da requisição_

```json
{
	"first_name": "jack",
}
```

_Formato de resposta_

```json
{
	"detail": "Invalid token."
}
```

#### Requisições com json invalido

_Formato da requisição_

```json
{
	"first_name": "CLAIRE"

}
```

_Formato de resposta_

```json
{
	"last_name": [
		"This field is required."
	],
	"password": [
		"This field is required."
	],
	"email": [
		"This field is required."
	]
}
```
#### Usuario ou item não encontrado 

_Formato da requisição_

```json
{
}
```

_Formato de resposta_

```json
{
	"detail": "Not found."
}
```
