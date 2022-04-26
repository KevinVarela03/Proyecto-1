import hashlib

usuarios_admin=[ 
    {
        'nombre':'Kevin',
        'apellido1':'Varela',
        'apellido2':'Rojas',
        'telefono':{64363005},
        'autenticacion':
        {
            'usuario':tuple(("KevinV",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest(),
            'tupla_contraseña':tuple((hashlib.md5('12345'.encode('ascii')).hexdigest(),)),
        }
    }
        ]
        
usuarios_estud=[ 
    {
        'nombre':'Anthony',
        'apellido1':'Jimenez',
        'apellido2':'Zamora',
        'telefono':{62713210},
        'autenticacion':
        {
            'usuario':tuple(("NoniJZ",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest(),
            'tupla_contraseña':tuple((hashlib.md5('12345'.encode('ascii')).hexdigest(),)),
        }
    }
        ]