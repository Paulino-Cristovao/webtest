from django.shortcuts import render

# Service definitions
SERVICES = [
    {
        'title': 'Visa Services',
        'url': 'visa_service',
        'icon': 'icons/visa.svg',
        'description': 'Read & download visa application forms.'
    },
    {
        'title': 'Passport Service',
        'url': 'passport_service',
        'icon': 'icons/passport.svg',
        'description': 'Apply or renew your passport online.'
    },
    {
        'title': 'Consular Assistance',
        'url': 'consular_assistance',
        'icon': 'icons/consular.svg',
        'description': 'Help with emergencies, notarization, legal docs.'
    },
    {
        'title': 'Trade & Investment',
        'url': 'trade_investment',
        'icon': 'icons/trade.svg',
        'description': 'Business, trade agreements, and investment info.'
    },
]

def service_list(request):
    """Render the services overview page."""
    return render(request, 'services/index.html', {'services': SERVICES})

def visa_service(request):
    """Handle visa service requests."""
    return render(request, 'services/visa.html')

def passport_service(request):
    """Handle passport service requests."""
    return render(request, 'services/passport.html')

def consular_assistance(request):
    """Handle consular assistance requests."""
    return render(request, 'services/consular.html')

def trade_investment(request):
    """Handle trade and investment information requests."""
    return render(request, 'services/trade.html')
