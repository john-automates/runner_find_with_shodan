# Shodan IP Lookup Runner

A runner that uses the Shodan API to gather detailed information about any IP address. The runner generates a comprehensive Markdown report containing information about the target IP, including open ports, running services, and potential vulnerabilities.

## Features

- Retrieves detailed host information from Shodan
- Generates formatted Markdown reports
- Includes:
  - Basic IP information (organization, ISP, location)
  - Open ports list
  - Service details with version information
  - Service banners
  - Known vulnerabilities (if any)

## Requirements

- Shodan API key (get one at https://account.shodan.io/)
- Python with `shodan` package (automatically installed by runner)

## Usage

1. Enter the IP address you want to look up
2. Provide your Shodan API key
3. The runner will generate a markdown file in the `outputs` directory named `{ip_address}_shodan_results.md`

## Output Format

The generated report includes:

```markdown
# Shodan Results for {ip_address}

## Basic Information
- IP
- Organization
- ISP
- Country
- City
- Last Update

## Open Ports
- List of open ports

## Services
Details for each service including:
- Protocol
- Service name
- Version
- Banner data (if available)

## Vulnerabilities
- List of known vulnerabilities (if any)
```

## Notes

- The runner requires a valid Shodan API key
- API usage limits apply based on your Shodan subscription
- Some information might not be available for all IP addresses