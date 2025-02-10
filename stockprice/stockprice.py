import click 
import requests

@click.group()
def stockprice():
    '''commands to manage your assets'''
    pass

@click.group(name='get')
def get_group():
    '''Group of commands to get something'''
    pass


@click.command(name='price')
def get_stock_price():
    '''Gets the stock price'''
    result = requests.get("https://query1.finance.yahoo.com/v8/finance/chart/GME")
    result_dict=result.json()
    click.echo(result_dict['chart']['result'][0]['meta']['regularMarketPrice'])
get_group.add_command(get_stock_price)
stockprice.add_command(get_group)


if __name__ == '__main__':
    stockprice()