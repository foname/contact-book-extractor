# contact-book-extractor

This repo provides solutions for two problems: song decoder and contact extractor.
- Song decoder is a simple function to remove “WUB” from a string.
- Contact extractor is also simple function to extract contact information from a long text string.

## Python version
`2.7` and above

## System dependencies
`None`

## Database 
`No db is required`

## How to run the test suite
For song decoder
`python -m tests.test_song_decoder`

For contact extractor
`python -m tests.test_contact_extractor`

## How to use
For song decoder
```
    Returns a proper string without WUB.

    Parameters:
        str_input (str):The string contains information that need to be decoded.

    Returns:
        (str): Readable string 
```

For contact_extractor
```
    Returns a string that consist of phone number, name, and address.

    Parameters:
        str_input (str):The string contains un-organized contact information.
        phone_num (str):The string phone number ex."48-421-674-8974".

    Returns:
        (str):String of "Phone => {phone_number}, Name => {name}, Address => {address}")  
```
