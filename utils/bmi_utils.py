"""BMI calculation and analysis utilities."""

from typing import Dict, Tuple
import math


def calculate_bmi(height: float, weight: float, unit: str = 'metric') -> float:
    """
    Calculate BMI based on height and weight.
    
    Args:
        height: Height value
        weight: Weight value
        unit: 'metric' (cm, kg) or 'imperial' (inches, lbs)
    
    Returns:
        BMI value rounded to 2 decimal places
    """
    if unit == 'metric':
        # Height in cm, weight in kg
        height_m = height / 100
        bmi = weight / (height_m ** 2)
    else:
        # Height in inches, weight in lbs
        bmi = (weight / (height ** 2)) * 703
    
    return round(bmi, 2)


def get_bmi_category(bmi: float) -> Dict:
    """
    Get BMI category and health information.
    
    Args:
        bmi: BMI value
    
    Returns:
        Dictionary with category, color, and health info
    """
    if bmi < 18.5:
        return {
            'category': 'Underweight',
            'color': '#3b82f6',
            'emoji': '📉',
            'health_status': 'Below Healthy Weight',
            'risks': ['Nutrient deficiencies', 'Weak immune system', 'Reduced bone density'],
            'recommendations': [
                'Increase calorie intake with nutritious foods',
                'Eat protein-rich foods',
                'Consult a nutritionist for personalized diet plan',
                'Exercise regularly to build muscle mass'
            ]
        }
    elif bmi < 25:
        return {
            'category': 'Normal Weight',
            'color': '#10b981',
            'emoji': '✅',
            'health_status': 'Healthy Weight Range',
            'risks': [],
            'recommendations': [
                'Maintain current weight through balanced diet',
                'Continue regular exercise routine',
                'Regular health checkups'
            ]
        }
    elif bmi < 30:
        return {
            'category': 'Overweight',
            'color': '#f59e0b',
            'emoji': '⚠️',
            'health_status': 'Slightly Above Healthy Weight',
            'risks': ['Type 2 diabetes', 'Heart disease', 'High blood pressure'],
            'recommendations': [
                'Reduce calorie intake moderately',
                'Increase physical activity to 30-60 minutes daily',
                'Include more fruits and vegetables',
                'Limit sugary drinks and processed foods',
                'Consult a healthcare provider for guidance'
            ]
        }
    else:
        return {
            'category': 'Obese',
            'color': '#ef4444',
            'emoji': '🚨',
            'health_status': 'Above Healthy Weight Range',
            'risks': ['Type 2 diabetes', 'Heart disease', 'Sleep apnea', 'Joint problems', 'Certain cancers'],
            'recommendations': [
                'Create a structured weight loss plan',
                'Consult a doctor or nutritionist',
                'Start with moderate exercise, gradually increase',
                'Track food intake and calories',
                'Join a weight loss program or support group',
                'Address any underlying health conditions'
            ]
        }


def get_ideal_weight_range(height: float, unit: str = 'metric') -> Dict:
    """
    Get ideal weight range for a given height.
    
    Args:
        height: Height value
        unit: 'metric' (cm) or 'imperial' (inches)
    
    Returns:
        Dictionary with ideal weight range
    """
    if unit == 'metric':
        # Height in cm
        height_m = height / 100
        min_weight = 18.5 * (height_m ** 2)
        max_weight = 24.9 * (height_m ** 2)
    else:
        # Height in inches
        min_weight = (18.5 * (height ** 2)) / 703
        max_weight = (24.9 * (height ** 2)) / 703
    
    unit_label = 'kg' if unit == 'metric' else 'lbs'
    
    return {
        'min': round(min_weight, 2),
        'max': round(max_weight, 2),
        'unit': unit_label,
        'range_text': f"{round(min_weight, 1)} - {round(max_weight, 1)} {unit_label}"
    }


def get_bmi_progress(current_bmi: float, target_bmi: float) -> Dict:
    """
    Calculate progress towards target BMI.
    
    Args:
        current_bmi: Current BMI value
        target_bmi: Target BMI value
    
    Returns:
        Progress information
    """
    difference = abs(current_bmi - target_bmi)
    progress_percentage = max(0, min(100, (1 - (difference / 10)) * 100))
    
    return {
        'difference': round(difference, 2),
        'progress_percentage': round(progress_percentage, 1),
        'direction': 'increase' if target_bmi > current_bmi else 'decrease' if target_bmi < current_bmi else 'maintain'
    }


def get_health_metrics(bmi: float) -> Dict:
    """
    Get comprehensive health metrics based on BMI.
    
    Args:
        bmi: BMI value
    
    Returns:
        Dictionary with health metrics
    """
    category_info = get_bmi_category(bmi)
    
    return {
        'bmi': bmi,
        'category': category_info['category'],
        'health_status': category_info['health_status'],
        'risks': category_info['risks'],
        'recommendations': category_info['recommendations'],
        'color': category_info['color'],
        'emoji': category_info['emoji']
    }
