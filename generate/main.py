import click
import faker

faker = faker.Faker()


def generate_csv(count):
    """Generate CSV data."""
    import csv

    from io import StringIO
    output = StringIO()

    writer = csv.writer(output)
    writer.writerow(['Name', 'Email', 'Salary'])
    for _ in range(count):
        writer.writerow([faker.name(), faker.email(), faker.random_number(digits=5)])

    return output.getvalue()


def generate_xml(count):
    """Generate XML data."""
    from dicttoxml import dicttoxml

    data = {'entries': []}
    for _ in range(count):
        entry = {
            'name': faker.name(),
            'email': faker.email(),
            'salary': faker.random_number(digits=5)
        }
        data['entries'].append(entry)

    xml_data = dicttoxml(data, custom_root='data', attr_type=False)
    return xml_data.decode('utf-8')


@click.command()
@click.option('--count', default=1, help='Number entries to generate.')
@click.option('--type', default="csv", help='Type of data to generate, CSV, XML. Defaults to CSV.')
@click.option('--outfile', prompt='Where would you like to save the file', help='The output filename.')
def generate(count, type, outfile):
    """Simple program to generate data."""
    if type.lower() == "csv":
        data = generate_csv(count)
    elif type.lower() == "xml":
        data = generate_xml(count)
    else:
        raise ValueError("Unsupported type. Please use 'csv' or 'xml'.")

    with open(outfile, 'w', newline='') as outfile:
        outfile.write(data)


if __name__ == '__main__':
    generate()
