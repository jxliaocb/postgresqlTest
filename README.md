# My Django Project

This is my blog  project with Django and postgresql. It does cool stuff!

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Create a database (testdb) in porgresql.
5. Create a .evn file  under the project folder and copy the following statesment to .env
```
SECRET_KEY=django-insecure-*$s4o3thx@%o4j6mcl4$))utbh!05&3xkgy6%no3rkoh=@tlb5
DEBUG=True
DB_NAME=testdb
DB_USER=postgre
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

6. Run migrations with `python manage.py migrate`.
7. Start the development server with `python manage.py runserver`.

## Usage

- Create a new user with the admin panel or the registration page.
- Explore the awesome features!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
