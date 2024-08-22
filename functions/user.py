import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

tableName = "UsuariosCIAT"

def agregarUsuario(db,user):

    table = db.Table(tableName)

    item={
        "id": user.id,
        "nombre":user.nombre,
        "parcelas": user.parcelas,
        "actividades": user.actividades,
        "contraseña": user.contraseña,
        "correo": user.correo
    }

    try:
        table.put_item(Item=item)
        return({"message":"item agregado correctamente"})
    except (NoCredentialsError, PartialCredentialsError):
        return("Error: No se encontraron las credenciales de AWS.")
    except Exception as e:
        return(f"Error al insertar el ítem: {e}")

def obtenerUsuarios(db):
    table = db.Table(tableName)
    response = table.scan()
    print(response)
    usuarios = response['Items']
    print(usuarios)
    return usuarios

def obtenerUsuarioID(db, id):

    table = db.Table(tableName)
    response = table.get_item(Key={ 'id': id  })
    print(response)
    return response["Item"]