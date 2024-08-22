import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from functions.user import obtenerUsuarioID

tableName = "UsuariosCIAT"

def agregarActividad(db,actividad, id):

    table = db.Table(tableName)

    user = obtenerUsuarioID(db, id)

    listaParcelas = list(user["actividades"]) 

    listaParcelas.append(dict(actividad))

    user["actividades"] = listaParcelas

    try:
        table.put_item(Item=user)
        return({"message":"item agregado correctamente"})
    except (NoCredentialsError, PartialCredentialsError):
        return("Error: No se encontraron las credenciales de AWS.")
    except Exception as e:
        return(f"Error al insertar el ítem: {e}")

def obtenerActividades(db, id):

    table = db.Table(tableName)
    response = table.get_item(Key={ 'id': id  })
    print(response)
    return response["Item"]["actividades"]