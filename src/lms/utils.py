def validate_book_data(book: dict):
    errors = {}
    title = book['title'].strip()
    author = book['author'].strip()
    desc = book['description'].strip()

    # validate title
    if len(title) == 0 or len(title) > 200:
        errors['title'] = f"`title` must not empty, neither will exceed char len of 200: {title}"

    if len(author) == 0 or len(author) > 100:
        errors['author'] = f"`author` must not be empty, neither will exceed 100 chars"

    # desc need not be validated
    if errors:
        errors['data'] = book
    return errors


def del_values_by_key(d: dict, *args):
    for arg in args:
        if arg in d:
            del d[arg]
