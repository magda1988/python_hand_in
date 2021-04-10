import scrapper
import writer


def prepare_data():
    print("Data is being prcessed. Please, wait...")

    scrapper.get_cellphones()
    writer.save_cellphones(scrapper.cellphones)


def get_all():
    all_cellphones = writer.get_all()
    all_cellphones_DTO = []
    for c in all_cellphones:
        phone_DTO = cell_to_DTO(c)
        all_cellphones_DTO.append(phone_DTO)
    return all_cellphones_DTO


def add_new(cellphone_DTO):
    cellphone_DTO["cell_id"] = None
    cell_phone = cell_from_DTO(cellphone_DTO)
    return cell_to_DTO(writer.add_new(cell_phone))


def cell_to_DTO(cell):
    cell_DTO = {}
    cell_DTO["name"] = cell[1]
    cell_DTO["price"] = int(cell[2])
    return cell_DTO


def cell_from_DTO(cell_DTO):
    cell = (None, cell_DTO["name"], cell_DTO["price"])
    return cell
