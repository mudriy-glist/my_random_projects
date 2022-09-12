import datetime
from unittest import result


def main():
    file = open("./example.log", "r")
    lines = file.read().splitlines()
    file.close()
    all_values_dict = {}
    result = []
    counter = 0

    for line in lines:
        if not line:
            continue

        columns = [col.strip() for col in line.split(" ") if col]

        date_str = columns[3].split(":")[0].replace("[", "")
        date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        name = columns[6].split("/")[1]
        response_code = columns[8]
        val_byte = int(columns[9])
        val_mb = val_byte / 1048576

        if date_obj.year not in all_values_dict:
            all_values_dict[date_obj.year] = {}
        if date_obj.strftime("%B") not in all_values_dict[date_obj.year]:
            all_values_dict[date_obj.year][date_obj.strftime("%B")] = {}
        all_values_dict[date_obj.year][date_obj.strftime("%B")][counter] = {
            "name": name,
            "response_code": response_code,
            "val_mb": val_mb,
        }
        counter += 1

    for key_year, value_year in all_values_dict.items():
        for key_month, value_month in value_year.items():
            all_names = []
            temp_dict = {}
            size_list = []
            for _, v in value_month.items():
                all_names.append(v["name"])

            uniq_names = set(all_names)
            all_val_mb = []

            temp_dict["weather"] = []
            for uniq_name in uniq_names:
                for _, v in value_month.items():
                    if v["name"] == uniq_name:
                        all_val_mb.append(v["val_mb"])
            
                

                # TODO pick top 5
                size_list.append(sum(all_val_mb))
                temp_dict["weather"].append(
                    {
                        "mean_MB": sum(all_val_mb) / len(all_val_mb),
                        "name": uniq_name,
                        "stddev_MB": "TODO",
                        "total_GB": sum(all_val_mb),
                    }
                )
            

            print(size_list)
            temp_dict["month"] = key_month
            # TODO implement non ascii
            temp_dict["non_ascii"] = []
            # TODO implement logic for requests
            temp_dict["requests"] = {
                "percent_success": "TODO",
                "success": "TODO",
                "total": "TODO",
            }
            temp_dict["year"] = key_year

            while len(temp_dict["weather"]) > 5:
                for k, v in temp_dict["weather"].items():
                    if v["total_GB"] == min(size_list):
                        temp_dict["weather"].remove()

            result.append(temp_dict)
    

if __name__ == "__main__":
    main()