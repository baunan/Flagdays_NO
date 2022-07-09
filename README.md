Under utarbeidelse

# Flaggdager Norge

Sensor with official flagdays in Norway, with a option to add your own (birthdays etc.)

## Credits
Data is from [Regjeringen.no](https://www.regjeringen.no/no/dep/ud/dep/norges-flagg-forskrift/id449230/).

Sunrises and sunsets in the future is provided by [Sunrise-Sunset](https://sunrise-sunset.org/api) API.

For installation instructions [see this guide](https://hacs.xyz/docs/faq/custom_repositories).
## Quick start
Add the following to your configuration.yaml
```yaml
flagdays_no:
  # Optional entries
  
  # Create attributes with specified offset in minutes
  # These are to be used as triggers in automatiions
  offset: 10
  
  # List of flags that we own and wish to use
  flags:
    - pride
    - Jolly Roger
    - Sami

  # List of custom events
  # Required: name and date
  # Optional: flag
  events:
    - name: Jolly Roger Memorial Day
      date: 01-01-2022
      flag: Jolly Roger
    - name: Oslo Pride
      date: 01-08-2004
      calculate_years: false
    - name: Tim Berners Lee Birthday
      date: 08-06-1955
    - name: Ada Lovelace Birthday
      date: 10-12-1815
```
## State and attributes
State is the number of days to the event

### Attributes

| Attribute name             | Example value                             | Description                        |
|----------------------------|-------------------------------------------|------------------------------------|
| event_name                 | H.M. kong Harald Vs fødselsdag            | Name of the event                  |
| date_str                   | 21. februar                               | Nice TTS date of the event         |
| date                       | 21-2-2022                                 | Date of the event                  |
| flag                       | Norgesflagg                               | Name of flag to use                |
| flag_up_time               | 08:42                                     | Time to hoist the flag             |
| flag_down_time             | 16:02                                     | Time to pull the flag              |
| flag_up_time_trigger       | 08:32                                     | Trigger to use for flag up         |
| flag_down_time_trigger     | 15:22                                     | Trigger to use for flag down       |
| timestamp                  | 1644046920                                | Timestamp of the event             |
| days_to_event              | 13                                        | Days to the event                  |
| years_to_celebrate         | 5                                         | Years passed on a custom event     |
| half_mast                  | false                                     | Flag at half mast?                 |
| half_mast_all_day          | false                                     | Flag at half mast all day?         |
| up_at_night                | false                                     | Flag allowed to be up at night?    |
| attribution                | Created by B Aunan                        | Name of the creator                |
