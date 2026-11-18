
import boto3
import csv
import io
from collections import defaultdict

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = event['bucket']
    file_key = event['key']

    # Read Starbucks CSV from S3
    response = s3.get_object(
        Bucket=bucket_name,
        Key=file_key
    )

    csv_content = response['Body'].read().decode('utf-8-sig')

    reader = csv.DictReader(io.StringIO(csv_content))

    # Store category statistics
    categories = defaultdict(lambda: {
        'count': 0,
        'total_calories': 0,
        'caffeine_values': []
    })

    for row in reader:

        category = row['Beverage_category'].strip()

        calories = float(row['Calories'])

        caffeine_text = row['Caffeine (mg)'].strip()

        categories[category]['count'] += 1
        categories[category]['total_calories'] += calories

        # Ignore caffeine values such as "Varies"
        try:
            caffeine = float(caffeine_text)
            categories[category]['caffeine_values'].append(caffeine)
        except (ValueError, AttributeError):
            pass

    # Create output CSV
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        'Beverage_Category',
        'Beverage_Count',
        'Average_Calories',
        'Average_Caffeine_mg'
    ])

    for category, data in sorted(categories.items()):

        count = data['count']

        average_calories = round(
            data['total_calories'] / count, 2
        )

        caffeine_values = data['caffeine_values']

        if caffeine_values:
            average_caffeine = round(
                sum(caffeine_values) / len(caffeine_values), 2
            )
        else:
            average_caffeine = 'N/A'

        writer.writerow([
            category,
            count,
            average_calories,
            average_caffeine
        ])

    # Upload processed summary to S3
    output_key = 'processed-data/starbucks_category_summary.csv'

    s3.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=output.getvalue().encode('utf-8'),
        ContentType='text/csv'
    )

    return {
        'statusCode': 200,
        'message': 'Starbucks nutrition data processed successfully',
        'output_file': output_key,
        'categories_processed': len(categories)
    }
