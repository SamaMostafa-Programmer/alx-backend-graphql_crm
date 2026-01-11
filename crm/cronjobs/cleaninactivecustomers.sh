#!/bin/bash

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

DELETED=$(python manage.py shell << EOF
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer

one_year_ago = timezone.now() - timedelta(days=365)
qs = Customer.objects.filter(orders__isnull=True, created_at__lt=one_year_ago)
count = qs.count()
qs.delete()
print(count)
EOF
)

echo "$TIMESTAMP - Deleted customers: $DELETED" >> /tmp/customercleanuplog.txt
