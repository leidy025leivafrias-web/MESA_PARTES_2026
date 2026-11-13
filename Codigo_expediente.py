def Codigo_expediente(expedientes):
    if not expedientes:
        return "EXP001"

    max_num = 0
    for expediente in expedientes:
        codigo = expediente.get("codigo_expediente") or expediente.get("codigo","")

        if codigo.startswith("EXP"):
            try: 
                num = int(codigo.replace("EXP", ""))
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
                
    siguiente_num = max_num + 1
    return f"EXP{siguiente_num:03d}"