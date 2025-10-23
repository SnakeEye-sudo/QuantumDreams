from flask import Flask, render_template, request, jsonify
import json
import random
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Sample data storage (in production, use a proper database)
dreams_data = []
stats_data = {
    'total_dreams': 0,
    'quantum_coherence_avg': 0.0,
    'visualization_views': 0
}

@app.route('/')
def home():
    """Home page with project overview and navigation"""
    return render_template('home.html')

@app.route('/dream-input')
def dream_input():
    """Dream input form page"""
    return render_template('dream_input.html')

@app.route('/submit-dream', methods=['POST'])
def submit_dream():
    """Process dream submission"""
    dream_text = request.form.get('dream_text', '')
    dream_intensity = request.form.get('intensity', 5)
    
    # Generate quantum-inspired analysis
    quantum_coherence = random.uniform(0.1, 1.0)
    dream_dimensions = random.randint(3, 11)
    
    dream_entry = {
        'id': len(dreams_data) + 1,
        'text': dream_text,
        'intensity': int(dream_intensity),
        'quantum_coherence': quantum_coherence,
        'dimensions': dream_dimensions,
        'timestamp': datetime.now().isoformat()
    }
    
    dreams_data.append(dream_entry)
    stats_data['total_dreams'] += 1
    stats_data['quantum_coherence_avg'] = sum(d['quantum_coherence'] for d in dreams_data) / len(dreams_data)
    
    return jsonify({'success': True, 'dream_id': dream_entry['id']})

@app.route('/visualization')
def visualization():
    """Dream visualization page"""
    stats_data['visualization_views'] += 1
    return render_template('visualization.html', dreams=dreams_data)

@app.route('/stats')
def stats():
    """Statistics and analytics page"""
    return render_template('stats.html', stats=stats_data, dreams=dreams_data)

@app.route('/api/dream-data')
def get_dream_data():
    """API endpoint for dream data"""
    return jsonify(dreams_data)

if __name__ == '__main__':
    app.run(debug=True)
